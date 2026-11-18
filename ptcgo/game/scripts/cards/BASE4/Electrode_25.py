from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d3987b2f-795c-5cb9-b8c9-25a6f32e7247",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="BASE4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Buzzap",
            game_text="At any time during your turn (before your attack), you may Knock Out Electrode and attach it to 1 of your other Pok\u00e9mon. If you do, choose a type of Energy. Electrode is now an Energy card of that type (instead of a Pok\u00e9mon) that provides 2 energy. This power can't be used if Electrode is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Electric Shock",
            game_text="Flip a coin. If tails, Electrode does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)