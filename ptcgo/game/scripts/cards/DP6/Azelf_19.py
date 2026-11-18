from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8e35115-b718-5a85-b387-e8b9348694b8",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Ability(
            title="Time Walk",
            game_text="Once during your turn, when you put Azelf from your hand onto your Bench, you may look at all of your face-down Prize cards. If you do, you may choose 1 Pok\u00e9mon you find there, show it to your opponent, and put it into your hand. Then, choose 1 card in your hand and put it as a Prize card face down.",
            effect=unimplemented,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)