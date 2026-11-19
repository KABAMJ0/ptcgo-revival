from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def core_enforcer(ctx):
    """Printed 150; then discard a Darkness and a Fairy Energy from this
    Pokemon (each one only if it is attached)."""
    await ctx.deal_damage()
    for type_value in (PokemonTypes.DARKNESS.value, PokemonTypes.FAIRY.value):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card, t=type_value: energy_provides_type(card, t),
            prompt="Choose an Energy to discard from this Pokémon")


card = PokemonCardDef(
    guid="2ebabc9a-56c4-5acc-beb3-38b820577284",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    family_id=718,
    abilities=[
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Core Enforcer",
            game_text="Discard a Darkness Energy and a Fairy Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=core_enforcer,
        ),
    ],
)