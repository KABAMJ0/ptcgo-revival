from ptcgo.game.card_effects.passives_common import boost_own_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f519eec-9dad-5527-b10a-fd6bc4449c90",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Ability(
            title="High Density Armor",
            game_text="If this Pok\u00e9mon has full HP, any damage done to this Pok\u00e9mon by an opponent's attack is reduced by 50 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=boost_own_next_turn(40, attack_title="Overdrive Smash"),
        ),
    ],
)