from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, self_energy_discard_attack

card = PokemonCardDef(
    guid="1ac58205-d4cd-5887-b0e5-e438cca0e17f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensClaydol.Name",
    display_name="Steven's Claydol",
    searchable_by=["Steven's Claydol", "Stage 1", "StevensClaydol"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Clay Blast",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)