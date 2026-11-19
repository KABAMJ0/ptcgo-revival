from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="c63bb9f5-e67b-56ff-bff3-2dacf08baf2d",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotEX.Name",
    display_name="Pidgeot-EX",
    searchable_by=["Pidgeot-EX", "Basic", "EX", "PidgeotEX"],
    subtypes=["Basic", "EX"],
    collector_number=64,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=18,
    abilities=[
        Attack(
            title="Mirror Move",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does the same amount of damage to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Feather Lance",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=snipe_attack(20, pool="bench", count=1, apply_modifiers=False),
        ),
    ],
)