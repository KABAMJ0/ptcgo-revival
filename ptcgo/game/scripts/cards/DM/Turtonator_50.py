from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def explosive_jet(ctx):
    """Discard any amount of Fire Energy from your Pokemon, then 50 for each."""
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon) if _fire_energy(energy)]
    discarded = []
    if pool:
        discarded = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose any amount of Fire Energy to discard")
        if discarded:
            await ctx.discard_cards(list(discarded))
    if discarded:
        await ctx.deal_damage(50 * len(discarded))

card = PokemonCardDef(
    guid="be18cf41-d9be-5af8-b7fa-c9ee1c4d775d",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=776,
    abilities=[
        Attack(
            title="Explosive Jet",
            game_text="Discard any amount of Fire Energy from your Pok\u00e9mon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=explosive_jet,
        ),
    ],
)