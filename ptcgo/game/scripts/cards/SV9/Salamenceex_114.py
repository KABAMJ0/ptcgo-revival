from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, spread_damage

card = PokemonCardDef(
    guid="6ad55bd5-4b16-5654-8291-b02865cd5d2a",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=114,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Wide Blast",
            game_text="This attack does 50 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=spread_damage(50, side="opponent"),
        ),
        Attack(
            title="Dragon Impact",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)