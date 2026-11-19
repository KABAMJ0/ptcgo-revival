from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, condition_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _opponent_has_darkness_energy(ctx) -> bool:
    return any(
        energy_provides_type(energy, PokemonTypes.DARKNESS.value)
        for pokemon in ctx.opponent_pokemon_in_play()
        for energy in ctx.attached_energies(pokemon)
    )


card = PokemonCardDef(
    guid="173b6403-ea6f-5f52-8af6-fcc7c356f3e9",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Punishing Slap",
            game_text="If any of your opponent's Pok\u00e9mon have any Darkness Energy attached to them, this attack does 60 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_opponent_has_darkness_energy, 60),
        ),
    ],
)