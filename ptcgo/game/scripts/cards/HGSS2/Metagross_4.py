from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="075abd3a-710f-5873-a42b-cdc8e360510c",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Psychic Float",
            game_text="If you have any Psychic Energy attached to your Active Pok\u00e9mon, the Retreat Cost for that Pok\u00e9mon is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Pulse Blast",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Double Leg Hammer",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 40 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=unimplemented,
        ),
    ],
)