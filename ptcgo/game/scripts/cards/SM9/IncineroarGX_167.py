from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, damage_counters_on, damage_per

card = PokemonCardDef(
    guid="1a976804-65b4-54be-a8e6-2e65abb93c2b",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarGX.Name",
    display_name="Incineroar-GX",
    searchable_by=["Incineroar-GX", "Stage 2", "GX", "IncineroarGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=167,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Scar Charge",
            game_text="Once during your turn (before your attack), you may put 3 damage counters on this Pok\u00e9mon. If you do, search your deck for up to 3 Darkness Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Punch",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=discard_opponent_energy_attack(1, special_only=True),
        ),
        Attack(
            title="Darkest Tornado-GX",
            game_text="This attack does 50 more damage for each damage counter on this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 50, base=10),
        ),
    ],
)