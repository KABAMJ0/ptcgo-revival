from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca79a578-7a16-5a69-a96c-131054d0e7d7",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigoex.Name",
    display_name="Flamigo ex",
    searchable_by=["Flamigo ex", "Basic", "ex", "Flamigoex"],
    subtypes=["Basic", "ex"],
    collector_number=160,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=973,
    abilities=[
        Attack(
            title="Precise Beak",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=recoil_attack(30),
        ),
    ],
)