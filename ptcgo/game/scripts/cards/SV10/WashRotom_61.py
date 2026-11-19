from ptcgo.game.card_effects.attacks_common import damage_per, count_in_play, has_tool
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="3093cf24-86c2-5444-a8c9-a4196cce7ac4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WashRotom.Name",
    display_name="Wash Rotom",
    searchable_by=["Wash Rotom", "Basic", "WashRotom"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=479,
    abilities=[
        Attack(
            title="Manual Wash",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=heal_targets(10, scope="each_own"),
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", has_tool), 30),
        ),
    ],
)