from ptcgo.game.card_effects.attacks_common import damage_per, count_bench
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="faf14e04-ba83-566e-8e6f-ffc6b8b226bd",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_bench("opponent"), 30),
        ),
        Attack(
            title="Foul Play",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)