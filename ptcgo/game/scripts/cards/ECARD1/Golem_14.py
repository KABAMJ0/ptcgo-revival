from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="600e5df8-62e6-5848-bdb6-97bae410d401",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Ability(
            title="Rock Body",
            game_text="All damage done by attacks to Golem is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Tumble",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)