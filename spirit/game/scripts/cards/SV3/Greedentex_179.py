from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="375e4387-e4b0-5c4f-a032-64b815f47880",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedentex.Name",
    display_name="Greedent ex",
    searchable_by=["Greedent ex", "Stage 1", "ex", "Tera", "Greedentex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=179,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Attack(
            title="Never Ever Enough",
            game_text="Look at the top 3 cards of your deck. You may put those cards into your hand. If you don't, discard those cards and draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Slip 'n' Roll",
            game_text="During your next turn, this Pok\u00e9mon can't use Slip 'n' Roll.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)