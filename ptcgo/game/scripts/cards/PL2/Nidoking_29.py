from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="893e5c1e-7bf9-53da-bd87-c7e96d1e1ecc",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Territoriality",
            game_text="If your Active Pok\u00e9mon is damaged by an opponent's attack (even if that Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon. You can't put more than 2 damage counters in this way.",
            effect=unimplemented,
        ),
        Attack(
            title="Fling Away",
            game_text="If your opponent has any Benched Pok\u00e9mon, this attack's base damage is 30 instead of 60 and this attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Giga Horn",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)