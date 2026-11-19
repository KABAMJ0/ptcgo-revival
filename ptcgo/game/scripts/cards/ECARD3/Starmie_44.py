from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="20020c6f-540d-5e19-920b-296975f08eea",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="This attack does 10 damage plus 20 more damage for each Water Energy attached to Starmie but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per_extra_energy(20, energy_type=PokemonTypes.WATER, cap=40, base=10),
        ),
        Attack(
            title="Core Blast",
            game_text="This attack does 30 damage plus 20 more damage for each Special Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
