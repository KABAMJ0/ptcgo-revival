from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3672eb4e-022a-589a-93ff-943293a3bd6c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HippowdonLVX.Name",
    display_name="Hippowdon LV.X",
    searchable_by=["Hippowdon LV.X", "Level-Up", "HippowdonLVX"],
    subtypes=["Level-Up"],
    collector_number=107,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    family_id=449,
    abilities=[
        Ability(
            title="Sand Reset",
            game_text="Once during a game on your turn (before your attack), each player shuffles all cards in play (excluding Pok\u00e9mon and Supporter cards) into his or her deck. You can't use more than 1 Sand Reset Pok\u00e9-Power each game.",
            effect=unimplemented,
        ),
        Attack(
            title="Double Shoot",
            game_text="Discard 2 Fighting Energy attached to Hippowdon and choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 40 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)