from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_in_play
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
card = PokemonCardDef(
    guid="d8865575-3328-549b-8052-89939c4223e6",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Rapid Strike", "Falinks"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=7,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Rapid Strike Squad",
            game_text="This attack does 20 damage for each of your Rapid Strike Pok\u00e9mon in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(
                count_in_play("mine", lambda p: "Rapid Strike" in subtypes_for(p.archetype_id)),
                20,
            ),
        ),
    ],
)