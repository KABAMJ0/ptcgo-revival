from ptcgo.game.card_effects.passives_common import guts_survive_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b699deb-a960-5de1-944a-5d88186526ce",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Durable Body",
            game_text="If this Pok\u00e9mon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pok\u00e9mon is not Knocked Out and its remaining HP becomes 10 instead.",
            passive=guts_survive_passive(hp_floor=10, flip=True, title="Durable Body"),
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
