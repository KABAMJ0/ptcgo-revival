from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="2705daa9-3f3e-5049-a1f8-b32e43132516",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "ex", "Charizardex"],
    subtypes=["Stage 2", "ex"],
    collector_number=161,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Brave Wing",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Explosive Vortex",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=330,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)