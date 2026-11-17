from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="729d4c52-67e8-5cbd-95ee-521f14c8505b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi ◇",
    searchable_by=["Jirachi \u25c7", "Basic", "Prism Star", "Jirachi"],
    subtypes=["Basic", "Prism Star"],
    collector_number=97,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Upon a Star",
            game_text="If you took this Pok\u00e9mon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench and take 1 more Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Perish Dream",
            game_text="This Pok\u00e9mon is now Asleep. At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            effect=unimplemented,
        ),
    ],
)