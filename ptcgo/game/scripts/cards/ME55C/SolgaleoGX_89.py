from ptcgo.game.card_effects.support_common import search_attach_energy, is_energy
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="295dd898-bdcf-5d29-93b7-e53619d37437",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=89,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=791,
    abilities=[
        Ability(
            title="Ultra Road",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sunsteel Strike",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=self_energy_discard_attack(all_energy=True),
        ),
        Attack(
            title="Sol Burst-GX",
            game_text="Search your deck for up to 5 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=search_attach_energy(predicate=is_energy, count=5, to_self=True),
        ),
    ],
)