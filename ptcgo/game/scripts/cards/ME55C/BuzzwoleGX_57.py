from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d8bcd33-4501-524a-906e-66cf5483afd3",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BuzzwoleGX.Name",
    display_name="Buzzwole-GX",
    searchable_by=["Buzzwole-GX", "Basic", "GX", "BuzzwoleGX"],
    subtypes=["Basic", "GX"],
    collector_number=57,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=794,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Knuckle Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Absorption-GX",
            game_text="This attack does 40 damage for each of your remaining Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)