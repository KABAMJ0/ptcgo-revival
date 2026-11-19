from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="49e7263c-403a-554f-9e43-fa764e92dbff",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatrex.Name",
    display_name="Feraligatr ex",
    searchable_by=["Feraligatr ex", "Stage 2", "ex", "Feraligatrex"],
    subtypes=["Stage 2", "ex"],
    collector_number=103,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Overpowering Fang",
            game_text="As long as Feraligatr ex is your Active Pok\u00e9mon, each player's Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Powers or Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Tsunami",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Sore Spot",
            game_text="Does 70 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)