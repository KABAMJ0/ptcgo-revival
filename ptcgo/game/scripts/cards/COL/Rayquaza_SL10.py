from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def inferno_spear(ctx):
    """Printed 100, then discard a Fire Energy and a Lightning Energy attached
    to Rayquaza."""
    await ctx.deal_damage()
    for type_value in (PokemonTypes.FIRE.value, PokemonTypes.LIGHTNING.value):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card, t=type_value: energy_provides_type(card, t),
            prompt="Discard the printed Energy attached to Rayquaza")

card = PokemonCardDef(
    guid="7291fc7a-ad8e-5faf-bcf2-f39260678536",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Inferno Spear",
            game_text="Discard a Fire Energy and a Lightning Energy attached to Rayquaza.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=inferno_spear,
        ),
    ],
)