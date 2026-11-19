from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cec094e5-d20f-51f8-8a6a-bfbfeb1402cd",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Mirror Move",
            game_text="If Pidgeot was damaged by an attack during your opponent's last turn, this attack does the same amount of damage done to Pidgeot to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)