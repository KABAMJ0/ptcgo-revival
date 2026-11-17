from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75cf17c3-1619-5a18-8fc1-2423a28c634b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorioex.Name",
    display_name="Oricorio ex",
    searchable_by=["Oricorio ex", "Basic", "ex", "Oricorioex"],
    subtypes=["Basic", "ex"],
    collector_number=18,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Ability(
            title="Excited Turbo",
            game_text="As often as you like during your turn, if you have any Fire Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to 1 of your Benched Fire Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)