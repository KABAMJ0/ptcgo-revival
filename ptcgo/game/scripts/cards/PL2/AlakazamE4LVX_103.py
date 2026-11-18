from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="061350c4-3df0-5cee-8e0d-412c830c1ccf",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamE4LVX.Name",
    display_name="Alakazam E4 LV.X",
    searchable_by=["Alakazam E4 LV.X", "Level-Up", "SP", "AlakazamE4LVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=103,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamE4.Name",
    family_id=65,
    abilities=[
        Ability(
            title="Damage Switch",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon SP to another of your Pok\u00e9mon SP. This power can't be used if Alakazam E4 is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)