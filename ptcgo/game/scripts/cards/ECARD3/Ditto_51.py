from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import def_for


async def _copy(ctx):
    defender = ctx.defender
    if defender is None:
        return
    attacks = [ability for ability in getattr(def_for(defender.archetype_id), "abilities", [])
               if isinstance(ability, Attack)]
    if not attacks:
        return
    picked = await ctx.choose_attack_to_copy(
        [(defender, attack) for attack in attacks], "Choose an attack to copy")
    if picked is None:
        return
    await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="b0c38a19-55fe-51b8-a52b-44d71f3fcbdb",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Prismatic Body",
            game_text="Each basic Energy card attached to Ditto provides every type of Energy but provides only 1 Energy at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Copy copies that attack. This attack does nothing if Ditto doesn't have the Energy necessary to use that attack. (You must still do anything else required in order to use that attack.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_copy,
        ),
    ],
)