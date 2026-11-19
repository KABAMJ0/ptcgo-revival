from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="b5231a1f-91f8-5f72-948d-f820bda029f6",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistcha.Name",
    display_name="Sinistcha",
    searchable_by=["Sinistcha", "Stage 1", "Sinistcha"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=place_counters(4, target="choose_any_opponent"),
        ),
        Attack(
            title="Spill the Tea",
            game_text="Discard up to 3 Grass Energy cards from your Pok\u00e9mon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)