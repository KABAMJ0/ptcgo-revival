from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="f648e738-19a9-573d-82f9-30b003807972",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name",
    display_name="Scovillain",
    searchable_by=["Scovillain", "Stage 1", "Scovillain"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Grass and Fire type.",
            effect=unimplemented,
        ),
        Attack(
            title="Spicy Headbutt",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)