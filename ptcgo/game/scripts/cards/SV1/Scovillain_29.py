from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="70079681-4130-537b-91ef-f1ace7347bd1",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name",
    display_name="Scovillain",
    searchable_by=["Scovillain", "Stage 1", "Scovillain"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Attack(
            title="Hot Bite",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Super Spicy Breath",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)