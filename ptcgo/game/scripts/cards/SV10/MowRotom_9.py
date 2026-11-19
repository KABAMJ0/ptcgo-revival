from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack, damage_per, count_in_play, has_tool

card = PokemonCardDef(
    guid="ae260771-d991-5440-a484-40af7a9eda92",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic", "MowRotom"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=479,
    abilities=[
        Attack(
            title="Trimming Mower",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=discard_stadium_attack(),
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