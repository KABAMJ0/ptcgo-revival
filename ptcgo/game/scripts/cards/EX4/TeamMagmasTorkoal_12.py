from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7b98d2fe-a7e8-596b-9729-7eb2394f929a",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasTorkoal.Name",
    display_name="Team Magma's Torkoal",
    searchable_by=["Team Magma's Torkoal", "Basic", "TeamMagmasTorkoal"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Magma Burn",
            game_text="Discard the top card from your opponent's deck, and flip a coin. If tails, discard a Fire Energy attached to Team Magma's Torkoal.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Hot Air",
            game_text="Discard a Fire Energy attached to Team Magma's Torkoal and your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)