from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90408161-960d-5568-9334-b4f92f834f68",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSneaselex.Name",
    display_name="Rocket's Sneasel ex",
    searchable_by=["Rocket's Sneasel ex", "Basic", "ex", "RocketsSneaselex"],
    subtypes=["Basic", "ex"],
    collector_number=103,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. If you do, this attack does 10 damage to the new Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Dark Ring",
            game_text="Does 30 damage plus 10 more damage for each of your Darkness Pok\u00e9mon in play.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)