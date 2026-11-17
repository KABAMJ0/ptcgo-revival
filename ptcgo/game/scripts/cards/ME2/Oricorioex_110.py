from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="27623938-4395-54be-a348-de7ff4e82c35",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorioex.Name",
    display_name="Oricorio ex",
    searchable_by=["Oricorio ex", "Basic", "ex", "Oricorioex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
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