from ptcgo.game.card_effects.attacks_common import damage_counters_on
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1ebf1a3-23d0-5f5e-bdc6-be1feb50ebe8",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Ability(
            title="Building Spite",
            game_text="Once during your turn (before your attack), you may put 1 damage counter on this Pok\u00e9mon.",
            effect=damage_per(damage_counters_on("self"), 30),
        ),
        Attack(
            title="Anguish Cry",
            game_text="This attack does 30 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)