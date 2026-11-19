from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="5b2c19f5-54af-5b72-95b2-f409fd1f5b1c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=104,
    abilities=[
        Attack(
            title="Burdensome Bone",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=lock_self_attack(),
        ),
    ],
)