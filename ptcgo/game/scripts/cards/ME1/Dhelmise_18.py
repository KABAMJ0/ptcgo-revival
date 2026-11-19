from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, stadium_in_play_cond


card = PokemonCardDef(
    guid="fc496cda-eb3e-5862-8305-ade4c25fead6",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Earthen Power",
            game_text="If you have a Stadium in play, this attack does 50 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(stadium_in_play_cond, 50),
        ),
    ],
)