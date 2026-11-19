from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52669517-e280-58c5-b766-f243f7b6c806",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampertex.Name",
    display_name="Swampert ex",
    searchable_by=["Swampert ex", "Stage 2", "ex", "Swampertex"],
    subtypes=["Stage 2", "ex"],
    collector_number=95,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=260,
    abilities=[
        Attack(
            title="Hyper Pump",
            game_text="Does 20 damage plus 20 more damage for each basic Energy attached to Swampert ex but not used to pay for this attack's Energy cost. You can't add more than 80 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per_extra_energy(20, base=20),
        ),
        Attack(
            title="Crushing Wave",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. After doing damage, flip a coin. If heads, your opponent discards an Energy card, if any, attached to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(40, pool="any"),
        ),
    ],
)