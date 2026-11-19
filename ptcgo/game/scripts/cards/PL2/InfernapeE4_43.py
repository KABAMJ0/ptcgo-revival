from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="64a3dd04-8f8e-55a6-a1b5-568975ab5956",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeE4.Name",
    display_name="Infernape E4",
    searchable_by=["Infernape E4", "Basic", "SP", "InfernapeE4"],
    subtypes=["Basic", "SP"],
    collector_number=43,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=392,
    abilities=[
        Attack(
            title="Split Bomb",
            game_text="Choose 2 of your opponent's Pok\u00e9mon. This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="any", count=2, apply_modifiers=False),
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)