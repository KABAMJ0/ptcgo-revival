from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="0f51215c-aa14-548a-8826-5eb24f8e9110",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2", "Annihilape"],
    subtypes=["Stage 2"],
    collector_number=100,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Tantrum",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=condition_attack(SpecialConditions.CONFUSED, self_conditions=(SpecialConditions.CONFUSED,)),
        ),
        Attack(
            title="Destined Fight",
            game_text="Both Active Pok\u00e9mon are Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)