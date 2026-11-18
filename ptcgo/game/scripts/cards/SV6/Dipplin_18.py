from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28baeadd-75e0-5a8c-b77d-9c531ac9bb84",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1", "Dipplin"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Festival Lead",
            game_text="If Festival Grounds is in play, this Pok\u00e9mon may use an attack it has twice. If the first attack Knocks Out your opponent's Active Pok\u00e9mon, you may attack again after your opponent chooses a new Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Do the Wave",
            game_text="This attack does 20 damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)