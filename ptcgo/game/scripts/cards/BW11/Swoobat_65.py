from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.pokemon import is_psychic_energy
from ptcgo.game.card_effects.support_common import search_attach_energy

card = PokemonCardDef(
    guid="6889a587-ae58-5528-a6a3-2cf50ece087c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Energy Gift",
            game_text="Flip a coin. If heads, search your deck for 2 Psychic Energy cards and attach them to your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=search_attach_energy(
                is_psychic_energy, count=2, distribute=True)),
        ),
        Attack(
            title="Heart Stamp",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)