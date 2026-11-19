from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def prehistoric_call(ctx) -> None:
    """From the discard pile: put this Pokemon on the bottom of the deck."""
    if not await ctx.ask_yes_no(
            "Put this Pokémon on the bottom of your deck?"):
        return
    await ctx.put_on_bottom_of_deck(ctx.source)


card = PokemonCardDef(
    guid="140b4aa8-4420-5d84-8bdf-4699910a2063",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Restored", "Archen"],
    subtypes=["Restored"],
    collector_number=53,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PlumeFossil.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Prehistoric Call",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            effect=prehistoric_call,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)