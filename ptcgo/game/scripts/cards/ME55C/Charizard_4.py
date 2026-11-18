from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cab5932e-5845-5f6f-94f6-33942bf28222",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="As often as you like during your turn (before your attack), you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy cards attached to Charizard in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)