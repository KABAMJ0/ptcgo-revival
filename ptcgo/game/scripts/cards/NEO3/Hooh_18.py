from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def rainbow_burn(ctx):
    """Printed 30 plus 10 for each TYPE of basic Energy attached to Ho-Oh."""
    types = set()
    for energy in ctx.attached_energies(ctx.attacker):
        if is_basic_energy_card(energy):
            types.update(energy.get_attribute(AttrID.POKEMON_TYPES) or [])
    await ctx.deal_damage(30 + 10 * len(types))

card = PokemonCardDef(
    guid="2deff919-9ea6-5755-b211-f13c53158418",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Rainbow Burn",
            game_text="This attack does 30 damage plus 10 more damage for each type of Basic Energy card, if any, attached to Ho-Oh.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            damage_operator="+",
            effect=rainbow_burn,
        ),
    ],
)