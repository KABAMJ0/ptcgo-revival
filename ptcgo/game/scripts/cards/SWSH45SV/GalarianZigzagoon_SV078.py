from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="f057b0d4-4022-50e9-b3c0-e654583a6da5",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    display_name="Galarian Zigzagoon",
    searchable_by=["Galarian Zigzagoon", "Basic", "GalarianZigzagoon"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=263,
    abilities=[
        Ability(
            title="Headbutt Tantrum",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)