from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a789f6d-896b-5fe8-bf30-005e68505e70",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTarountula.Name",
    display_name="Team Rocket's Tarountula",
    searchable_by=["Team Rocket's Tarountula", "Basic", "TeamRocketsTarountula"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=917,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)