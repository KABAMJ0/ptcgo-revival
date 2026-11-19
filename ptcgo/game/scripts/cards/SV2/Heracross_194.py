from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="15b05cbf-f4f3-50a3-a9c7-b179111201c3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=194,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
        Attack(
            title="Smashing Horn",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 3},
            damage=110,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)