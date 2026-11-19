from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="ee1c4c48-438e-5e01-b4a6-b366db648982",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CameruptG.Name",
    display_name="Camerupt G",
    searchable_by=["Camerupt G", "Basic", "SP", "CameruptG"],
    subtypes=["Basic", "SP"],
    collector_number=19,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=323,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Earth Power",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=unimplemented,
        ),
    ],
)