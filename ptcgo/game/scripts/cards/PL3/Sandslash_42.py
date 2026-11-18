from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7260c0e3-6a66-5084-bf01-28dfb08509a8",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Dig Down",
            game_text="Once during your turn (before your attack), you may look at the top 5 cards in your deck. Choose as many Fighting Energy cards as you like, show them to your opponent, and put them into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward. This power can't be used if Sandslash is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Needle",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)